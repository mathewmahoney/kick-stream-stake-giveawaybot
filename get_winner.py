  def fetch_random():
            try:
                import re
                numbers = []
                for entry in self.entries:
                    nums = [int(n) for n in re.findall(r'\d+', entry)]
                    if nums:
                        numbers.extend(nums)
                
                max_val = max(numbers) if numbers else len(self.entries)
                
                # Using the exact API format requested. 
                # We keep num=10 as requested, but only use the first number returned.
                url = f"https://www.random.org/integers/?num=1&min=1&max={max_val}&col=1&base=10&format=plain&rnd=new"
                response = requests.get(url)
                
                # The API returns 10 numbers separated by newlines. We just need the first one.
                random_num = int(response.text.strip().split('\n')[0])

                # Match the random number to the entries
                winner = None
                # Case 1: Exact match with the string value of the random number
                for entry in self.entries:
                    if entry.strip() == str(random_num):
                        winner = entry
                        break
                
                # Case 2: Number is found within the entry string
                if not winner:
                    for entry in self.entries:
                        if str(random_num) in re.findall(r'\d+', entry):
                            winner = entry
                            break
                
                # Case 3: Fallback to simple list index matching
                if not winner:
                    idx = (random_num - 1) % len(self.entries)
                    winner = self.entries[idx]

                self.root.after(0, self.show_winner, winner, random_num)
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Draw Error", f"Failed to draw winner: {str(e)}"))
                self.root.after(0, lambda: self.status_label.config(text="Status: Draw Failed", foreground="red"))
