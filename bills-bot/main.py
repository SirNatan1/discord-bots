import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

intents = discord.Intents.all()
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
    reset_bills()

def reset_bills():
    global bills, unexpected_bills
    bills = {key: 0 for key in bills}
    unexpected_bills = [] 

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    scheduler.add_job(send_bills_list, 'cron', day=1, hour=9, minute=0)
    scheduler.add_job(send_monthly_summary, 'cron', day=28, hour=20, minute=00)
    scheduler.start()

@client.event
async def on_message(message):
    if message.content.startswith("!pay"):
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

    elif message.content.startswith("!unexpected"):
        try:
            _, amount, *description = message.content.split()
            amount = float(amount)
            description = " ".join(description)
            unexpected_bills.append((amount, description))  
            await message.channel.send(f"Unexpected payment of ₪{amount} for: {description}.")
        except ValueError:
            await message.channel.send("Invalid format. Use: !unexpected <amount> <description>")

    elif message.content.startswith("!summary"):
        total = sum(bills.values()) + sum(unexpected_bills)
        await message.channel.send(f"Total payments for the month: ₪{total}")

    elif message.content.startswith("!bills"):
        bill_list = "\n".join([f"{bill}: ₪{amount}" for bill, amount in bills.items()])
        unexpected_list = "\n".join([f"{description}: ₪{amount}" for amount, description in unexpected_bills])
        message_text = f"📋 **Current bills:**\n{bill_list}\n\n💸 **Unexpected bills:**\n{unexpected_list}"
        await message.channel.send(message_text)

client.run('<bot_token>')  # Replace with your actual bot token
