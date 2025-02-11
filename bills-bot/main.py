import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Store payments for each bill
payments = {
    "electricity": [],
    "water": [],
    "property_tax": [],
    "gas": [],
    "internet": [],
    "house_committee": [],
    "mortgage": [],
    "unexpected": []  # Track unexpected bills
}

@bot.command()
async def pay(ctx, bill: str, amount: float):
    """Log a payment for a regular bill."""
    bill = bill.lower()
    if bill in payments:
        payments[bill].append(amount)
        await ctx.send(f"{ctx.author.name} paid ${amount} for {bill}.")
    else:
        await ctx.send(f"Unknown bill: {bill}. Please use a valid bill name.")

@bot.command()
async def pay_unexpected(ctx, amount: float, *, description: str):
    """Log a payment for an unexpected bill."""
    payments["unexpected"].append({"amount": amount, "description": description})
    await ctx.send(f"{ctx.author.name} paid ${amount} for an unexpected bill: {description}.")

@bot.command()
async def summary(ctx):
    """Summarize the total payments for the month."""
    total = {bill: sum(amounts) if isinstance(amounts, list) else sum(item["amount"] for item in amounts) for bill, amounts in payments.items()}
    summary_msg = "**Monthly Payment Summary:**\n"
    for bill, total_paid in total.items():
        if bill == "unexpected":
            unexpected_summary = "\n".join([f"- {item['description']}: ${item['amount']}" for item in payments["unexpected"]])
            summary_msg += f"{bill.capitalize()}:\n{unexpected_summary}\nTotal: ${total_paid}\n"
        else:
            summary_msg += f"{bill.capitalize()}: ${total_paid}\n"
    await ctx.send(summary_msg)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run('<YOUR_BOT_TOKEN>')
