def generate_invitations(template, attendees):
	try:
		if not isinstance(template, str):
			print(f"Error: Invalid template type: {type(template).__name__}")
			return
		if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
			print(f"Error: Invalid attendees type: {type(attendees).__name__}")
			return
		if template == "":
			print("Template is empty, no output files generated.")
			return
		if len(attendees) == 0:
			print("No data provided, no output files generated.")
			return

		for idx, attendee in enumerate(attendees, start=1):
			content = template
			for placeholder in ["name", "event_title", "event_date", "event_location"]:
				value = attendee.get(placeholder)
				if value is None:
					value = "N/A"
				content = content.replace("{" + placeholder + "}", str(value))
			filename = f"output_{idx}.txt"
			with open(filename, "w") as f:
				f.write(content)
	except Exception as e:
		print(f"An error occurred: {e}")
