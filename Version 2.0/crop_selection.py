from rich.console import Console

console = Console()

# Define rotation plans for different crops
rotation_plans = {
    "corn": {
        "rotation": ["soybeans", "wheat", "alfalfa"],
        "benefits": ["helps control corn rootworm and corn earworm populations", "reduces nitrogen leaching", "improves soil health"]
    },
    "soybeans": {
        "rotation": ["corn", "wheat", "alfalfa"],
        "benefits": ["fixes nitrogen in the soil", "improves soil health", "reduces weed pressure"]
    },
    "wheat": {
        "rotation": ["corn", "soybeans", "alfalfa"],
        "benefits": ["improves soil health", "reduces pest pressure", "adds organic matter to soil"]
    },
    "alfalfa": {
        "rotation": ["corn", "soybeans", "wheat"],
        "benefits": ["fixes nitrogen in the soil", "improves soil health", "reduces weed pressure"]
    }
}

# Get user input for a crop
crop = input("Enter a crop: ")

# Check if the crop is in the rotation plans
if crop.lower() in rotation_plans:
    console.print(f"[bold]Crop rotation plan for {crop}:[/bold]")
    for i, crop in enumerate(rotation_plans[crop.lower()]["rotation"]):
        console.print(f"{i+1}. {crop}")
    console.print("\n[bold]Benefits of rotating with this crop:[/bold]")
    for benefit in rotation_plans[crop.lower()]["benefits"]:
        console.print(f"- {benefit}")
else:
    console.print(f"[bold red]Error:[/bold red] Crop '{crop}' not found in rotation plans.")
