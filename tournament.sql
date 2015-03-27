-- Table definitions for the tournament project.
--

--  Players Table
DROP TABLE players cascade;
DROP TABLE matches cascade;

CREATE TABLE players (
    id serial,
    name text
);


--  Matches Table
CREATE TABLE matches (
    winner integer NOT NULL,
    loser integer NOT NULL
);

-- Scoreboard View
-- Creates a view containing player id, name, win count, loss count
create view scoreboard as 
    select  players.id, 
            players.name,
            (select count(winner) as wins from matches where winner = players.id),
            (select count(*) as total from matches where loser=players.id or winner=players.id) 
    from players 
    order by wins desc;
