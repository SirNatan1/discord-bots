# Apartment Cleaning Reminder Bot

This is a Discord bot designed to send scheduled reminders for cleaning tasks in your apartment. It helps keep track of daily, weekly, biweekly, monthly, quarterly, and yearly cleaning activities by sending notifications to a specified Discord channel.

## **Features**
- Sends scheduled cleaning reminders based on frequency (daily, weekly, biweekly, etc.).
- Helps maintain a clean and organized living space.
- Fully automated using APScheduler and Discord bot commands.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher
- A Discord account and a server where you want to add the bot

### **Step 1: Install Dependencies**
First, install the required Python libraries. Open your terminal (or command prompt) and run:

```bash
pip install discord.py
pip install APScheduler
```

### **Step 2: Set Up Your Discord Bot**
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application.
3. Add a bot to the application.
4. Copy the bot token (you will need this later).

### **Step 3: Configure the Bot**
1. Clone or download this repository.
2. Save the provided bot code in a file named `cleaning_bot.py`.
3. Open the file and replace `'YOUR_BOT_TOKEN'` with your bot token:

```python
client.run('YOUR_BOT_TOKEN')  # Replace this with your actual bot token
```

4. Replace `CLEANING_CHANNEL_ID` with the Discord channel ID where the bot should send cleaning reminders.

### **Step 4: Run the Bot**
Navigate to the folder where you saved `cleaning_bot.py` and run:

```bash
python cleaning_bot.py
```

If everything is set up correctly, you should see `Logged in as <bot_name>` in your terminal, indicating that the bot is running.

### **Step 5: Invite the Bot to Your Server**
1. Go to the **OAuth2** section in the Discord Developer Portal.
2. Under **OAuth2 URL Generator**, select:
   - Scopes: `bot`
   - Bot Permissions: `Send Messages`, `Read Message History`
3. Copy the generated URL and paste it into your browser to invite the bot to your server.

---

## **Cleaning Task Schedule**
The bot sends reminders for the following cleaning tasks:

### **Daily**
- Wash dishes / load dishwasher
- Wipe kitchen counters & table
- Quick wipe of stovetop & sink
- Take out trash if full or smelly
- 5-minute mess clean (put things back in place)
- Quick toilet brush if needed
- Make the bed

### **Weekly (Sunday at 10 AM)**
- Vacuum & mop floors
- Dust shelves, electronics, nightstands
- Scrub toilet, sink, shower/tub
- Wipe kitchen appliances & clean microwave
- Change bedsheets
- Wipe inside trash cans

### **Biweekly (1st and 15th at 2 PM)**
- Vacuum couch & under furniture
- Wipe doorknobs, light switches, handles
- Clean bathroom vent/fan
- Shake out/vacuum rugs & mats
- Wipe mirrors and glass

### **Monthly (1st at 2 PM)**
- Clean windows (inside)
- Descale showerhead & faucets
- Declutter cabinets & pantry
- Deep clean stove & oven
- Rotate mattress
- Clean chimney filters

### **Quarterly (Jan, Apr, Jul, Oct 1st at 10 AM)**
- Wash curtains & upholstery
- Deep clean fridge & freezer
- Check & unclog drains
- Clean balcony/patio area
- Deep clean chimney fan blades & housing

### **Yearly (Jan 1st at 9 AM)**
- Deep clean windows (inside & outside)
- Steam clean carpets & furniture
- Check & replace smoke detector batteries
- Clean behind large appliances
- Replace chimney charcoal filters if applicable

---

## **Customization**
If you want to modify the schedule, update the following lines in `cleaning_bot.py`:

```python
scheduler.add_job(send_cleaning_reminder, 'cron', day_of_week="*", hour=9, args=["daily"])
```

You can adjust `day_of_week`, `day`, `month`, and `hour` to fit your preferred schedule.

---

## **Contributing**
Feel free to contribute by submitting issues or pull requests to improve this bot!

---

Enjoy your cleaner and more organized living space! 🏡✨
