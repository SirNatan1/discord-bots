import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler

intents = discord.Intents.all()
client = discord.Client(intents=intents)
scheduler = AsyncIOScheduler()

CLEANING_CHANNEL_ID = 123456789012345678  # Replace with your actual channel ID

cleaning_tasks = {
    "daily": [
        "✅ Wash dishes / load dishwasher",
        "✅ Wipe kitchen counters & table",
        "✅ Quick wipe of stovetop & sink",
        "✅ Take out trash if full or smelly",
        "✅ 5-minute mess clean (put things back in place)",
        "✅ Quick toilet brush if needed",
        "✅ Make the bed"
    ],
    "weekly": [
        "🧹 Floors: Vacuum & mop",
        "🧽 Dusting: Shelves, electronics, nightstands",
        "🚽 Bathroom: Scrub toilet, sink, shower/tub",
        "🍽️ Kitchen: Wipe appliances, clean microwave, scrub sink",
        "🛏️ Bedroom: Change bedsheets",
        "🗑️ Trash Cans: Wipe inside"
    ],
    "biweekly": [
        "🛋️ Vacuum couch & under furniture",
        "🚪 Wipe doorknobs, light switches, handles",
        "🚿 Check & clean bathroom vent/fan",
        "🧺 Shake out/vacuum rugs & mats",
        "🪞 Glass & Mirrors: Wipe down"
    ],
    "monthly": [
        "🪟 Clean windows (inside)",
        "🚿 Descale showerhead & faucets",
        "📦 Declutter cabinets & pantry",
        "🍳 Deep clean stove & oven",
        "🛏️ Rotate mattress",
        "🧼 Chimney: Clean metal filters, wipe exterior & interior"
    ],
    "quarterly": [
        "🛋️ Wash curtains & upholstery",
        "🧼 Deep clean fridge & freezer",
        "🛠️ Check & unclog drains",
        "🪵 Wash balcony/patio area",
        "🌀 Chimney: Deep clean fan blades & housing"
    ],
    "yearly": [
        "🪟 Deep clean windows (inside & outside)",
        "🧼 Steam clean carpets & furniture",
        "🔋 Check & replace smoke detector batteries",
        "🧽 Clean behind large appliances",
        "🔄 Replace chimney charcoal filters if applicable"
    ]
}

async def send_cleaning_reminder(task_type):
    """Sends a cleaning reminder to the designated Discord channel."""
    channel = client.get_channel(CLEANING_CHANNEL_ID)
    if channel:
        tasks_list = "\n".join(cleaning_tasks[task_type])
        await channel.send(f"🧹 **{task_type.capitalize()} Cleaning Reminder:**\n{tasks_list}")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    scheduler.add_job(send_cleaning_reminder, 'cron', day_of_week="*", hour=9, args=["daily"])  # Daily at 9 AM
    scheduler.add_job(send_cleaning_reminder, 'cron', day_of_week="sun", hour=10, args=["weekly"])  # Weekly on Sunday at 10 AM
    scheduler.add_job(send_cleaning_reminder, 'cron', day="1,15", hour=14, args=["biweekly"])  # Every 2 weeks on 1st and 15th at 2 PM
    scheduler.add_job(send_cleaning_reminder, 'cron', day="1", hour=14, args=["monthly"])  # Monthly on the 1st at 2 PM
    scheduler.add_job(send_cleaning_reminder, 'cron', month="1,4,7,10", day="1", hour=10, args=["quarterly"])  # Quarterly on the 1st of Jan, Apr, Jul, Oct at 10 AM
    scheduler.add_job(send_cleaning_reminder, 'cron', month="1", day="1", hour=9, args=["yearly"])  # Yearly on Jan 1st at 9 AM

    scheduler.start()

client.run('YOUR_BOT_TOKEN')  # Replace with your bot token
