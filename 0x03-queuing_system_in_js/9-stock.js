import express from 'express';
import { createClient } from 'redis';

/**
 * A note to the task reviewer: I did not use `promisify`
 * because the Redis client get method being used already returns a Promise,
 * making it unnecessary to use promisify with it.
 * Starting from redis@4.0.0, the library has built-in support for Promises.
 */

const redisClient = createClient();

redisClient.on('error', (err) =>
  console.error(`Redis client not connected to the server: ${err}`)
);
redisClient.on('connect', () =>
  console.log('Redis client connected to the server')
);

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  const product = listProducts.find((item) => item.itemId === id);
  return product;
}

function reserveStockById(itemId, stock) {
  redisClient.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await redisClient.get(`item.${itemId}`);
  return parseInt(stock, 10);
}

const app = express();
const port = 1245;

redisClient.connect();

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentStock = product.initialAvailableQuantity - (reservedStock || 0);

  res.json({ ...product, currentQuantity: currentStock });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentStock = product.initialAvailableQuantity - (reservedStock || 0);

  if (currentStock < 1) {
    res.json({ status: 'Not enough stock available', itemId });
    return;
  }

  reserveStockById(itemId, (reservedStock || 0) + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => console.log('The server is running...'));
