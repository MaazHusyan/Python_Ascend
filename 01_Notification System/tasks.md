# 1: 🧪 SOLID Design Challenge: Notification System

Design a notification system that adheres to all 5 SOLID principles. Each task corresponds to one principle.
---
### ✅ Task 1: Single Responsibility Principle (SRP)
Design separate classes for each notification type — Email, SMS, Push — each with a single responsibility to send one type of notification.

### ✅ Task 2: Open/Closed Principle (OCP)
Ensure the system can be extended to support more notification types (e.g., WhatsApp, Slack) without modifying existing classes.

### ✅ Task 3: Liskov Substitution Principle (LSP)
Create a common base class or interface for all notification types. Any notification type should be usable in place of the base class without breaking functionality.

### ✅ Task 4: Interface Segregation Principle (ISP)
Avoid creating large interfaces. Each class should only implement methods it actually uses. Ensure no notification class is forced to implement irrelevant methods.

### ✅ Task 5: Dependency Inversion Principle (DIP)
The NotificationManager should depend on the Notifier abstraction, not on concrete implementations like Email or SMS. Use constructor injection to supply the dependency.

---

### 🎯 Objective:
Design a clean, extensible, and testable notification system applying all SOLID principles.

---

### 🧪 Submission:
- Write the solution in Python
- Ensure classes are clean and separated by responsibility
- Follow OOP best practices strictly
- No `if-else` logic to check notification type
- Use `abc` module for abstraction where needed
