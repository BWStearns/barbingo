# BAR BINGO (real name needed)

## Overview

### The App

Basically it's a game centered around a given bar. The bar can make squares for their establishment or allow them to be global for anyone to use. 

Customers can say "I'm at SomeBar, I want to play" and it will make a new card for that night out of the available global/bar specific squares. 

The idea is that it would be entertaining/might be good for some random or weekly kind of trivia-night-esque thing, get bingo get a drink, fill out the whole card get your tab half off, etc/whatever. Also since you can make bar specific stuff it tends towards encouraging regularism.

### Tech

Backend is written in Python/Django. Front end is going to be JS/HTML plus whatever kind of mobile client stuff we come up with.

#### Details

Since the idea is to mainly make it easy to play from a phone I was thinking write pretty much everything to be API driven from the start to avoid having to rewrite any backend stuff. Also this means we can play a bit more with the JS framework we pick or if we're really ambitious we can mess around with native mobile.

#### Stack
+ Python 2.7.5
+ Django 1.5
+ JS (because screw it, it owns the web)
+ Angular or Knockout?
    + Really anything other than Backbone, since the whole point of JS frameworks is to, you know, make JS NOT suck?
+ For mobile maybe http://phonegap.com/
    + Looks fairly easy and quick to get running

## Feature List

+ Actual Bingo Game - *in progress*
    + `best_contribution` square?
        + Patrons submit photos or something and ref picks?
    + Get models and stuff built out - *pretty much done*
        + Make a serialization method for all objects to avoid ad-hoc BS
    + Allow creation of squares
    + Generate unique gameboards
        + .... and for groups
    + Limit
    + JSON endpoints
        + Unscrew ordering -*done*
        + Generally unscrew and standardize API
            + Unscrew after most of it is built
            + All ideas for an actual strategy welcomed
        + Get all boards for a game - *done*
        + Get board - *done*
        + Claim square as found - *done*
        + Mark square as confirmed - *done*
        + `require_proof` Squares
            + recieve photos - *needed*
            + show photos - *needed*
            + status and confirm for proof squares - *needed*
+ User Models and Permissions - *in progress*
    + Figure out how permissions work - *in progress*
+ Bar models to own/limit games - *in progress*
+ 'Evidence'
    + Allow certain squares to require evidence, like a picture or something.
    + Have an account associated with the bar be able to confirm the square.
    + Allow the bar to have access to the evidence photos for promo purposes?
+ Get the front-end sorted out 
    + Make the web interface so that a bar can set something up - *done*
        + Make the add/delete squares views
        + Make the game management views
    + Make it at the very least mobile friendly, ideally a semi-native client.
+ More stuff I haven't bothered to write here yet.