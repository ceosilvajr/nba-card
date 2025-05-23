import save_to_pdf as pdf
import nba_player_card as card

# Main loop for user interaction
print("--- Welcome to the NBA Player Card Generator! ---")
print("This script uses AI to analyze NBA players and create detailed reports, saved as PDF files.")

while True:
    answer = input('Create a new NBA Card? Y for yes, anything else to quit: ')
    if answer != 'Y':
        print("Exiting the NBA Player Card Generator. Goodbye!")
        break  # Exit the loop if the user doesn't enter 'Y'

    name = input('Enter NBA Player Name: ').strip()

    if not name:
        print("Player name cannot be empty. Please try again.")
        continue  # Skip to the next iteration if no name is provided

    print(f"\nGenerating report for {name}...\n")
    report = card.generate(name)
    print(report)

    # Check if the report generation was successful before creating PDF
    if not report.startswith("Error:"):
        pdf.save(name, report)
    else:
        print("\nPDF file was not generated due to an error in report creation.")

    print("\n" + "=" * 70 + "\n")  # Add a clear separator for multiple reports
