
# Apartment Management Discord Bot

This is a Discord bot to help manage apartment-related tasks, such as tracking bills and payments. It allows you and your partner to keep track of regular and unexpected bills in your apartment, log payments, and view a summary at the end of the month.

### Features:
- Log payments for regular bills (electricity, water, gas, etc.).
- Log unexpected bills with a description and amount.
- Summarize all payments for the month.
- Interactive commands for easy management.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher
- A Discord account and a server where you want to add the bot

### **Step 1: Install Dependencies**
First, you need to install the required Python libraries. Open your terminal (or command prompt) and run the following command:

```bash
pip install discord.py
```

### **Step 2: Set Up Your Discord Bot**
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application.
3. Add a bot to the application.
4. Copy the bot token (you will use this token in the bot code).

### **Step 3: Configure the Bot**
1. Clone or download this repository.
2. Save the provided bot code in a file named `apartment_bot.py`.
3. Open the file and replace `'YOUR_BOT_TOKEN'` with the bot token you copied earlier:

```python
bot.run('YOUR_BOT_TOKEN')  # Replace this with your actual bot token
```

### **Step 4: Run the Bot**
In your terminal, navigate to the folder where you saved `apartment_bot.py` and run the following command:

```bash
python apartment_bot.py
```

You should see a message like `Logged in as <bot_name>` indicating that the bot is running.

### **Step 5: Invite the Bot to Your Server**
1. Go to the **OAuth2** section in the Discord Developer Portal (where you created your bot).
2. Under **OAuth2 URL Generator**, select:
   - Scopes: `bot`
   - Bot Permissions: `Send Messages`, `Read Message History`, `Manage Messages`, `Add Reactions` (you can adjust permissions as needed).
3. Copy the generated URL, paste it in your browser, and invite the bot to your Discord server.

---

## **Commands**

### **Log Payments**
- **`!pay <bill> <amount>`**  
  Logs a payment for a regular bill.  
  Example: `!pay electricity 50`

- **`!pay_unexpected <amount> <description>`**  
  Logs a payment for an unexpected bill with a description.  
  Example: `!pay_unexpected 100 "Repair Costs"`

### **Get Payment Summary**
- **`!summary`**  
  Displays a summary of the total payments for regular and unexpected bills.

---

## **Bot Commands and Their Use**
### **Regular Bills**
You can log payments for the following regular bills:
- electricity
- water
- property tax
- gas
- internet
- committee
- mortgage

### **Unexpected Bills**
For unexpected bills (e.g., repairs, medical expenses), you can use the `!pay_unexpected` command. The bot will keep track of these bills with a description and their amounts.

---

## **Contributing**

Feel free to contribute to this project! You can submit issues or pull requests to help improve it.
