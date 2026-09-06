def explain_message(message, prediction):
    text = str(message).lower()
    reasons = []
    urgency = ["urgent", "immediately", "hurry", "act now", "limited time", "expires"]
    promotional = ["free", "winner", "won", "prize", "reward", "congratulations", "bonus", "cash"]
    links = ["click", "link", "visit", "http", "www."]
    security = ["verify", "confirm", "account", "password", "login", "suspended"]
    offers = ["offer", "discount", "sale", "deal", "claim"]
    if any(word in text for word in urgency): reasons.append("Urgency-based wording")
    if any(word in text for word in promotional): reasons.append("Promotional or prize-related language")
    if any(word in text for word in links): reasons.append("Suspicious link or call-to-action")
    if any(word in text for word in security): reasons.append("Account verification or security-related wording")
    if any(word in text for word in offers): reasons.append("Promotional offer language")
    if prediction == "spam" and not reasons: reasons.append("Message patterns associated with spam")
    if prediction == "ham" and not reasons: reasons.append("No strong spam indicators detected")
    return reasons

if __name__ == "__main__":
    message = "URGENT! You won a FREE prize. Click now to claim your reward!"
    prediction = "spam"
    print("Explanation:")
    for reason in explain_message(message, prediction): print("-", reason)
