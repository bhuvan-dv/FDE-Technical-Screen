# FDE Technical Screen – Package Sorting Function

## Objective
This project implements a function for Thoughtful’s robotic automation factory.  
The function is responsible for dispatching packages to the correct stack according to their **volume** and **mass**.  

## Rules
- A package is **bulky** if:
  - Its volume (Width × Height × Length) ≥ **1,000,000 cm³**, OR  
  - Any one of its dimensions ≥ **150 cm**.  
- A package is **heavy** if:
  - Its mass ≥ **20 kg**.  

### Stack Categories
- **STANDARD** → Package is **not bulky and not heavy**.  
- **SPECIAL** → Package is **either bulky or heavy**.  
- **REJECTED** → Package is **both bulky and heavy**.  

---

## Implementation
The function is implemented in Python:

```python
def sort(width: int, height: int, length: int, mass: int) -> str:
    """
    Classify the package into STANDARD, SPECIAL, or REJECTED.
    """
    volume = width * height * length
    bulky = volume >= 1_000_000 or (width >= 150 or height >= 150 or length >= 150)
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    return "SPECIAL" if bulky or heavy else "STANDARD"
