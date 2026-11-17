C:\Users\Alumno\Desktop\folder_structure_test\data\clean\data_.csv
from pathlib import Path

# base va a represntar la ruta de el proyecto
BASE = Path(__file__).resolve().parent.parent
print(BASE)

RAW = BASE / "data" / "raw"
CLEAN = BASE / "data" / "clean"

print(RAW)
print(CLEAN)