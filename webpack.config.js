const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'sparkrapp/static/scripts'),
    },
    watch: true,
    module: {

        rules: [

            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "sass-loader",
                ],
            },
        ],
    },
    plugins: [

        new MiniCssExtractPlugin({

            filename: "../styles/main.css",

        }),
    ],
};