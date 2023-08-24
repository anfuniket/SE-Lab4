class FlightTable:
    def __init__(self):
        self.data = [
            ("Mumbai", "India", "Sri Lanka", "DAY"),
            ("Delhi", "England", "Australia", "DAY-NIGHT"),
            ("Chennai", "India", "South Africa", "DAY"),
            ("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
            ("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
            ("Delhi", "India", "Australia", "DAY")
        ]

    def search_by_team(self, team):
        matches = [match for match in self.data if team in (match[1], match[2])]
        return matches

    def search_by_location(self, location):
        matches = [match for match in self.data if location == match[0]]
        return matches

    def search_by_timing(self, timing):
        matches = [match for match in self.data if timing == match[3]]
        return matches

def main():
    flight_table = FlightTable()

    while True:
        print("Search options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            team = input("Enter the team name: ")
            matches = flight_table.search_by_team(team)
        elif choice == "2":
            location = input("Enter the location: ")
            matches = flight_table.search_by_location(location)
        elif choice == "3":
            timing = input("Enter the timing: ")
            matches = flight_table.search_by_timing(timing)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

        if matches:
            print("Match Location\tTeam 01\tTeam 02\tTiming")
            for match in matches:
                print(f"{match[0]}\t{match[1]}\t{match[2]}\t{match[3]}")
        else:
            print("No matches found.")

if __name__ == "__main__":
    main()
