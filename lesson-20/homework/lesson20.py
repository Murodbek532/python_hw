import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")


# 1. Customer Purchases Analysis

invoices = pd.read_sql("""
    SELECT i.InvoiceId, i.CustomerId, i.Total, c.FirstName, c.LastName
    FROM invoices i
    JOIN customers c ON i.CustomerId = c.CustomerId
""", conn)

customer_spending = invoices.groupby(
    ["CustomerId", "FirstName", "LastName"]
)["Total"].sum().reset_index().rename(columns={"Total": "TotalSpent"})

top5_customers = customer_spending.sort_values(
    by="TotalSpent", ascending=False
).head(5)

print("Top 5 customers by total spending:")
print(top5_customers)

# 2. 


invoice_lines = pd.read_sql("""
    SELECT il.InvoiceLineId, il.InvoiceId, il.TrackId, t.AlbumId, i.CustomerId
    FROM invoice_items il
    JOIN tracks t ON il.TrackId = t.TrackId
    JOIN invoices i ON il.InvoiceId = i.InvoiceId
""", conn)

conn.close()

album_track_counts = invoice_lines.groupby("AlbumId")["TrackId"].nunique()

customer_album_tracks = invoice_lines.groupby(
    ["CustomerId", "AlbumId"]
)["TrackId"].nunique().reset_index()

customer_album_tracks["AlbumTrackCount"] = customer_album_tracks["AlbumId"].map(album_track_counts)
customer_album_tracks["FullAlbum"] = customer_album_tracks["TrackId"] == customer_album_tracks["AlbumTrackCount"]

customer_pref = customer_album_tracks.groupby("CustomerId")["FullAlbum"].all().reset_index()
customer_pref["Preference"] = customer_pref["FullAlbum"].map({True: "Full Albums", False: "Individual Tracks"})

preference_summary = customer_pref["Preference"].value_counts(normalize=True) * 100

print("\nCustomer purchase preferences (percent):")
print(preference_summary)
