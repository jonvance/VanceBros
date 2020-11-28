const express = require('express')
var cors = require('cors')
const app = express()
const port = 3000

const finnhub = require('finnhub');
 
const api_key = finnhub.ApiClient.instance.authentications['api_key'];
api_key.apiKey = "bv0s2c748v6u4eaccu5g" // Replace this
const finnhubClient = new finnhub.DefaultApi()

app.use(cors())

app.get('/', (req, res) => {

  // finnhubClient.companyNews("AAPL", "2020-01-01", "2020-05-01", (error, data, response) => {
  //   if (error) {
  //       res.json(error);
  //   } else {
  //       res.json(data)
  //   }
  // });

  finnhubClient.stockSymbols("US", (error, data, response) => {
    res.send(data)
});

})

app.listen(port, () => {console.log(`App listening at http://localhost:${port}`)})