# 🏦 Bank Management System - OOP Practice Tasks

## ✅ Phase 1: Core OOP Concepts

### 1. Class & Object
- [ ] Create a `BankAccount` class
- [ ] Define `__init__` with `account_holder`, `balance`
- [ ] Create two accounts and print their info

---

### 2. Encapsulation
- [ ] Make `balance` private
- [ ] Add `get_balance()` and `deposit()`/`withdraw()` methods with validation
- [ ] Prevent withdrawing if insufficient funds

---

### 3. Inheritance
- [ ] Create subclass `SavingsAccount` with interest rate
- [ ] Create subclass `CurrentAccount` with overdraft limit
- [ ] Override relevant methods (e.g., `withdraw()`)

---

### 4. Abstraction
- [ ] Create abstract base class `Account` using `ABC`
- [ ] Define abstract methods like `deposit()` and `withdraw()`
- [ ] Implement them in child classes (`SavingsAccount`, `CurrentAccount`)

---

### 5. Polymorphism
- [ ] Define a method `print_summary(account)` that works on any type of account
- [ ] Show runtime polymorphism with overridden methods

---

### 6. Getter & Setter
- [ ] Add `@property` for `account_holder`
- [ ] Add validation to setter (e.g., no numbers in name)

---

## ✅ Phase 2: SOLID Principles

### S — Single Responsibility Principle
- [ ] Create a class `TransactionLogger` that only logs transactions
- [ ] Keep transaction logic out of account class

---

### O — Open/Closed Principle
- [ ] Add `PremiumAccount` without modifying `Account` class
- [ ] Use inheritance to extend functionality

---

### L — Liskov Substitution Principle
- [ ] Replace any `Account` object with child class (`SavingsAccount`, etc.) without breaking logic

---

### I — Interface Segregation Principle
- [ ] Split interface if needed (e.g., create `InterestBearing` interface for interest-specific accounts only)

---

### D — Dependency Inversion Principle
- [ ] Create `NotificationManager` that depends on abstract class `Notifier`
- [ ] Implement `EmailNotifier`, `SMSNotifier`, etc.
- [ ] Inject dependency into account for alerts

---

## ✅ Bonus:
- [ ] Add CLI-style menu for deposit/withdraw
- [ ] Use composition to inject `TransactionLogger` and `Notifier`

---

## 📁 Structure Suggestion
