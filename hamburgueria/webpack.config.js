const path = require('path');

module.exports = {
  entry: './core/static/core/js/index.js',
  output: {
    path: path.resolve(__dirname, 'core/static/core/js/dist'),
    filename: 'bundle.js',
  },
  mode: 'development', // Modo
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};
