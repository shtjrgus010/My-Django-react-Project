# My Project

## 2024.11.01

### Common Model Field

- created_at
- updated_at

### Tweet Model Field

- payload(max_length=180)
- user: ForeignKey

### Like Model Field

- user: ForeignKey
- tweet: ForeignKey

### Requirements

- Use `abstract` classes
- Customize the `__str__` method of all classes.
