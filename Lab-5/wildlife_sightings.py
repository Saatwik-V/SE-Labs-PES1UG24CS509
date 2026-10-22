"""Wildlife sanctuary sightings logger and reporting script."""

import hashlib
import sqlite3


def init_db():
    """Initialize in-memory SQLite database and create table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE sightings ("
        "id INTEGER PRIMARY KEY, species TEXT, zone TEXT, count INTEGER)"
    )
    return connection


def log_sighting(connection, species, zone, count, extras=None):
    """Record a wildlife sighting in the database."""
    if extras is None:
        extras = {}
    connection.execute(
        "INSERT INTO sightings (species, zone, count) VALUES (?, ?, ?)",
        (species, zone, count)
    )
    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer):
    """Generate a short observer identifier from a name."""
    digest = hashlib.md5(
        observer.encode(), usedforsecurity=False
    ).hexdigest()
    return digest[:6]


def zone_summary(connection, zone):
    """Return total count of sightings for a given zone."""
    query = "SELECT SUM(count) FROM sightings WHERE zone = ?"
    row = connection.execute(query, (zone,)).fetchone()
    if row[0] is None:
        return 0
    return row[0]


def rarest(connection):
    """Find the species with the lowest total sighting count."""
    query = "SELECT species, SUM(count) FROM sightings GROUP BY species"
    rows = connection.execute(query).fetchall()
    rarest_species = min(rows, key=lambda r: r[1])
    return rarest_species[0]


def main():
    """Run sample sightings and print summary statistics."""
    conn = init_db()
    totals = log_sighting(conn, "Leopard", "North", 1)
    log_sighting(conn, "Chital", "North", 24, totals)
    log_sighting(conn, "Hornbill", "East", 3, totals)
    if len(totals) != 3:
        raise ValueError("Invalid totals count")
    print(observer_id("Arun"), zone_summary(conn, "North"), rarest(conn))


if __name__ == "__main__":
    main()
