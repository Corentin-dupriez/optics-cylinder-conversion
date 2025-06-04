# optics-cylinder-conversion

This Python script converts optical prescriptions between **negative cylinder** and **positive cylinder** formats, commonly used in ophtalmology and optometry. It helps eye care professionals, optical technicians, and developers working with optical data to quickly and accurately perform conversions.

---

## What it does

Given a prescription with 
- **Sphere**
- **Cylinder**
- **Axis**

It converts from: 
- **Negative cylinder notation** -> **Positive cylinder notation**
- or the reverse

  The mathematical transformation follows:
  new sphere = sphere + cylinder
  new cylinder = -cylinder
  new axis = axis + 90 (- 180 if the calculated axis is over 180)

  ---
  Example:

  Input (Negative cylinder):
  Sphere: - 2.00
  Cylinder: -1.50
  Axis: 180

  Output (Positive Cylinder):
  Sphere: -3.50
  Cylinder: +1.50
  Axis: 90

  ## Why this matters

  Some regions or professionals prefer prescriptions in **positive cylinder format** (e.g orthopists), while others use the **negative cylinder format** (e.g optometrists in the US).This tool ensures accurate conversion for interoperability or patient record translation.

  ## How to use
  1. Clone the repo or copy the script
  ```bash
  git clone https://github.com/Corentin-dupriez/optics-cylinder-conversion.git
  cd optics-cylinder-conversion
    ```
  2. Run the script
  ```bash
python cylindres.py
  ```

Follow the on-screen prompts to input values manually or import and use the functions in your own Python project.
