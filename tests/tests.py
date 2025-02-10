from rich.console import Console
from rich.table import Table

def key_log(id, username, key, expires_at, valid):
  console = Console()

  table = Table()

  table.add_column("ID", justify="left", no_wrap=True)
  table.add_column("USERNAME")
  table.add_column("KEY")
  table.add_column("VALIDITY")
  table.add_column("STATUS")

  table.add_row()
  table.add_row()
  table.add_row()
  table.add_row()
  table.add_row()

  console.print(table)
