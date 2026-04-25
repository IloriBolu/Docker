const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send("App is running rn ");
});


app.get("/healthz", (req, res) => {
  res.status(200).send("Yo healthz section ye");
});



app.listen(PORT, () => {
  console.log(`the server running on port ${PORT}`);
});