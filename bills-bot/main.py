import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import datetime

intents = discord.Intents.default()
intents.messages = True  # Allows the bot to receive messages
intents.guilds = True  # Allows the bot to see guilds
intents.message_content = True  # Required for reading message content

# Initialize the Discord client with intents
client = discord.Client(intents=intents)
scheduler = AsyncIOScheduler()

# Store bills and payments (you can replace this with your data storage solution)
bills = {
    "electricity": 0,
    "water": 0,
    "property_tax": 0,
    "gas": 0,
    "internet": 0,
    "committee": 0,
    "mortgage": 0
}

unexpected_bills = []

# Channel ID where you want the bot to send messages
BILLS_CHANNEL_ID = <channel ID>  # Replace with your channel ID

async def send_bills_list():
    channel = client.get_channel(BILLS_CHANNEL_ID)
    bill_list = "\n".join([f"{bill}" for bill in bills.keys()])
    await channel.send(f"Reminder, Bills to pay this month:\n{bill_list}")

async def send_monthly_summary():
    channel = client.get_channel(BILLS_CHANNEL_ID)
    total = sum(bills.values()) + sum(unexpected_bills)
    await channel.send(f"Monthly summary:\nTotal Payments: ₪{total}")
    # Reset bills for the new month
    reset_bills()

def reset_bills():
    global bills, unexpected_bills
    bills = {key: 0 for key in bills}  # Reset regular bills
    unexpected_bills = []  # Reset unexpected bills

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    scheduler.add_job(send_bills_list, 'cron', day=1, hour=9, minute=0)  # Sends bills list at 9:00 AM on the 1st of each month
    scheduler.add_job(send_monthly_summary, 'cron', day=28, hour=20, minute=00)  # Sends summary at 20:00 PM on the 28th (change as needed)
    scheduler.start()

@client.event
async def on_message(message):
    if message.content.startswith("!pay"):
        # Process regular bill payment
        try:
            _, bill, amount = message.content.split()
            amount = float(amount)
            if bill in bills:
                bills[bill] += amount
                await message.channel.send(f"Payment of ₪{amount} logged for {bill}.")
            else:
                await message.channel.send("Unknown bill.")
        except ValueError:
            await message.channel.send("Invalid format. Use: !pay <bill> <amount>")

    elif message.content.startswith("!pay_unexpected"):
        # Process unexpected bill payment
        try:
            _, amount, *description = message.content.split()
            amount = float(amount)
            description = " ".join(description)
            unexpected_bills.append(amount)
            await message.channel.send(f"Unexpected payment of ₪{amount} for: {description}.")
        except ValueError:
            await message.channel.send("Invalid format. Use: !pay_unexpected <amount> <description>")

    elif message.content.startswith("!summary"):
        # Show current summary
        total = sum(bills.values()) + sum(unexpected_bills)
        await message.channel.send(f"Total payments for the month: ₪{total}")

    elif message.content.startswith("!bills"):
        # Print all current bills and their amounts
        bill_list = "\n".join([f"{bill}: ₪{amount}" for bill, amount in bills.items()])
        unexpected_total = sum(unexpected_bills)
        message_text = f"📋 **Current bills:**\n{bill_list}\n\n💸 **Unexpected bills total:** ₪{unexpected_total}"
        await message.channel.send(message_text)

# Run the bot with your token
client.run('<bot_token>')  # Replace with your actual bot token
