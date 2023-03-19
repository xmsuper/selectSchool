const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    // 配置跨域
    proxy:{
        '/api':{
        // 需要代理的地址,这里设置的地址会代替axios中设置的baseURL
        target:'http://127.0.0.1:8000',
        // 是否允许接口跨域
        changeOrigin:true,
        // pathRewrite方法重写url
        pathRewrite:{
          // '^api':'/'重写之后url为http://127.0.0.1:8080/xxx
          '^/api':'http://127.0.0.1:8080/'
        }
      }
    }
  },

})
