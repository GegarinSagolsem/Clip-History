import tkinter as tk
import pyperclip
import textwrap  # <-- IMPORT THE NEW LIBRARY

# --- Configuration ---
HISTORY_LIMIT = 20
POLL_INTERVAL_MS = 500

# --- CONFIGURATION SETTINGS ---
PREVIEW_LINE_LIMIT = 3   # Max lines to show for multi-line snippets
SINGLE_LINE_CHAR_LIMIT = 100 # Max chars *before* we wrap it

# --- Core Logic Class ---
class ClipboardManager:
    """Manages the state of the clipboard history."""
    
    def __init__(self, history_limit=HISTORY_LIMIT):
        self.history = []
        self.last_item = self._get_clipboard_content()
        # Add the current item to history on startup if it's not empty
        if self.last_item:
            self.history.append(self.last_item)
        self.HISTORY_LIMIT = history_limit

    def _get_clipboard_content(self):
        """Safely gets text content from the clipboard."""
        try:
            return pyperclip.paste()
        except pyperclip.PyperclipException:
            # This can happen if the clipboard contains non-text (like an image)
            return None 

    def check_for_updates(self):
        """Checks if the clipboard has new content and updates history."""
        current_item = self._get_clipboard_content()
        
        # Add to history if:
        # 1. It's not empty (None)
        # 2. It's different from the last item
        if current_item and current_item != self.last_item:
            self.history.insert(0, current_item)
            self.last_item = current_item
            
            # Trim the history list if it's over the limit
            if len(self.history) > self.HISTORY_LIMIT:
                self.history.pop() # Removes the oldest item
                
            return True # Signal that the UI needs to update
        return False # No update needed

# --- UI Class ---
class Application(tk.Tk):
    """The main application window and UI controller."""
    
    # --- THIS IS THE FIXED LINE ---
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

        # --- Window Setup ---
        self.title("ClipHistory")
        self.geometry("450x550") # Width x Height

    def build_ui(self):
        """Clears and redraws the list of history items."""
        # Clear all old buttons
        for widget in self.winfo_children():
            widget.destroy()
            
        # Create a new button for each item in the manager's history
        for item in self.manager.history:
            
            # --- START OF NEW TEXTWRAP LOGIC ---
            
            # This will be the text we work with
            preview_text = item
            
            lines = item.splitlines()
            num_lines = len(lines)

            # Case 1: It's a single line AND it's too long
            if num_lines == 1 and len(item) > SINGLE_LINE_CHAR_LIMIT:
                # Use textwrap to automatically add newlines
                preview_text = textwrap.fill(item, width=SINGLE_LINE_CHAR_LIMIT)
            
            # Now, we re-check the lines on the (potentially) wrapped text
            lines = preview_text.splitlines()
            num_lines = len(lines)

            # Case 2: It now has too many lines (either originally or from wrapping)
            if num_lines > PREVIEW_LINE_LIMIT:
                truncated_lines = lines[:PREVIEW_LINE_LIMIT]
                display_text = "\n".join(truncated_lines) + "\n..."
            else:
                # Case 3: It's a short single line, or 2-3 lines. Perfect.
                display_text = preview_text
            
            # --- END OF NEW TEXTWRAP LOGIC ---

            button = tk.Button(
                self,
                text=display_text,
                command=lambda i=item: self.on_item_click(i),
                anchor='w', # Align text to the left (west)
                justify='left', # Justify multi-line text to the left
                padx=10
            )
            button.pack(fill='x', padx=5, pady=2) # Pack it into the window

    def poll_clipboard(self):
        """Periodically check the clipboard and update UI if needed."""
        if self.manager.check_for_updates():
            self.build_ui() # Re-draw the buttons if history changed
            
        # Schedule this function to run again after the interval
        self.after(POLL_INTERVAL_MS, self.poll_clipboard)

    def on_item_click(self, item):
        """Callback to copy an item back to the clipboard."""
        pyperclip.copy(item)

# --- Main Execution ---
if __name__ == "__main__":
    # This block only runs when the script is executed directly
    
    # 1. Create the logic manager
    clipboard_manager = ClipboardManager()
    
    # 2. Create the UI application
    app = Application(clipboard_manager)
    
    # 3. Build the initial UI
    app.build_ui()
    
    # 4. Start the clipboard monitoring loop
    app.poll_clipboard()
    
    # 5. Run the application's main event loop
    app.mainloop()