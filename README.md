# Blockchain - Explaination


## **Block**

A block is a record that is linked to it's predecesor successor with a unique hash.

## **Block Chain**

A block chain is a collection of these linked blocks. Block chains is required for Non-Fungible Tokens (NFTs) and Cryptocurrencies in their current form.


###  **Qualities of Blockchains**
* Immutiable
* Persistent
* Distrubuted

### **Proof of Work**
In order to keep a chronological history of previous blocks in the chain, a **nonce** is required. A nonce is the number of leading 0 bits when creating a new hash.

The number of leading bit is known as **difficulty**. Thus the amount of work for generating a new hash exponentially increases per block created. It also makes modifying previous blocks close to impossibile as you need to create the following blocks in the chain.

What you will find in this project is an example of simple block chain in Python using an **SHA-256** Hash.

### How to use

```python3 app.py```

This will run a flask server on port 5000 that with three end-points:

```POST /pay``` Send JSON data to simulate a purchase

```GET /chain``` Gives the current chain with all it's blocks

```POST /mine``` Takes all the transactions before the last mine and then creates a new block with it