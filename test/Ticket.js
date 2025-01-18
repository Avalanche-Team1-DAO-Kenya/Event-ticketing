const {expect} = require("chai");
const {ethers} = require("hardhat");
describe ("Ticket", () => {
    let Ticket, ticket, owner, addr1, addr2;

    beforeEach(async () => {
        // Get the ContractFactory and Signers here.
        Ticket = await ethers.getContractFactory("Ticket");
        [owner, addr1, addr2] = await ethers.getSigners();

        // Deploy the contract
        ticket = await Ticket.deploy("Ticket", "TKT");
        await ticket.deployed();
    });

    describe("Deployment",()=>{
        it("Set the correct name", async () => {
            expect(await ticket.name()).to.equal("Ticket");
        });
        
        it("Set the correct symbol", async () => {
            expect(await ticket.symbol()).to.equal("TKT");
        });

        it("Set the right owner", async () => {
            expect(await ticket.owner()).to.equal(owner.address);
        }); 
    });

    describe("Minting", () => {
        it("Should allow owner to mint tickets", async () => {
            const eventId = 1;
            const quantity = 5;
            const price = ethers.utils.parseEther("0.1");

            await ticket.createTickets(eventId, quantity, price);
            expect(await ticket.getTicketSupply(eventId)).to.equal(quantity);
        });

        it("Should not allow non-owners to mint tickets", async () => {
            const eventId = 1;
            const quantity = 100;
            const price = ethers.utils.parseEther("0.1");

            await expect(ticket.connect(addr1).createTickets(eventId, quantity, price)).to.be.revertedWith("Ownable: caller is not the owner");
        });
    });

    describe("Purchasing or Buying", () => {
        const eventId = 1;
        const quantity = 100;
        const price = ethers.utils.parseEther("0.1");

        beforeEach(async () => {
            await ticket.createTickets(eventId, quantity, price);
        });

        it("Should allow users to purchase tickets", async () => {
            const purchaseQuantity = 2;
            const totalPrice = price.mul(purchaseQuantity);

            await expect(
                ticket.connect(addr1).purchaseTicket(eventId, purchaseQuantity, {
                    value: totalPrice
                })
            ).to.emit(ticket, "TicketPurchased")
                .withArgs(addr1.address, eventId, purchaseQuantity);

            expect(await ticket.getTicketSupply(eventId)).to.equal(quantity - purchaseQuantity);
        });

        it("Should fail if insufficient payment is sent", async () => {
            const purchaseQuantity = 2;
            const insufficientPrice = price.mul(purchaseQuantity).sub(1);

            await expect(
                ticket.connect(addr1).purchaseTicket(eventId, purchaseQuantity, {
                    value: insufficientPrice
                })
            ).to.be.revertedWith("Insufficient payment");
        });

        it("Should fail if trying to purchase more tickets than available", async () => {
            const excessiveQuantity = quantity + 1;
            const totalPrice = price.mul(excessiveQuantity);

            await expect(
                ticket.connect(addr1).purchaseTicket(eventId, excessiveQuantity, {
                    value: totalPrice
                })
            ).to.be.revertedWith("Not enough tickets available");
        });
    });

    describe("Transfer", () => {
        it("Should allow ticket transfer between addresses", async () => {
            const eventId = 1;
            const quantity = 1;
            const price = ethers.utils.parseEther("0.1");

            await ticket.createTickets(eventId, quantity, price);
            await ticket.connect(addr1).purchaseTicket(eventId, 1, {
                value: price
            });

            const tokenId = await ticket.tokenOfOwnerByIndex(addr1.address, 0);
            await ticket.connect(addr1).transferFrom(addr1.address, addr2.address, tokenId);

            expect(await ticket.ownerOf(tokenId)).to.equal(addr2.address);
        })
    })
})