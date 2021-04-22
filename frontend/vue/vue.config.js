const path = require('path');

module.exports = {
    publicPath: '',
    outputDir: path.resolve(__dirname, '../web'),
    filenameHashing: false,
    pluginOptions: {
        i18n: {
            locale: 'ko',
            fallbackLocale: 'en',
            localeDir: 'locales',
            enableInSFC: true
        }
    },
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000',
                changeOrigin: true
            }
        }
    }
};
