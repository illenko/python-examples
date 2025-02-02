import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
payment_amounts = [250, 300, 280, 350, 400, 420, 380, 320, 270, 310, 360, 450]  # Example payment data

plt.plot(months, payment_amounts, color='blue', marker='o', linestyle='-', linewidth=2, label='Monthly Payments')

plt.xlabel("Month")
plt.ylabel("Payment Amount ($)")
plt.title("Monthly Payment History")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
