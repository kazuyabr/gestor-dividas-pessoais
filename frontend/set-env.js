const dotenv = require('dotenv');
const config = require('./environment.config.js');

dotenv.config();

const port = config.port;
process.argv.push(`--port=${port}`);

require('@angular/cli/bin/ng');
