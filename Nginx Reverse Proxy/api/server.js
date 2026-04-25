const express = require("express");
const app = express();

const PORT = 3000;

app.get("/api/items", (req, res) => {
  res.json([
    { id: 1, name: "bolu" },
    { id: 2, name: "ilori" }
  ]);
});

app.get("/health", (req, res) => {
  res.json({ status: "healthy yk" });
});

app.listen(PORT, () => {
  console.log(`API running on port ${PORT}`);
});