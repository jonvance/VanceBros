const express = require('express')
var cors = require('cors')
const app = express()
const port = 3000

app.use(cors())

app.get('/', (req, res) => {
  res.send('Backend Homepage')
})

app.listen(port, () => {console.log(`App listening at http://localhost:${port}`)})