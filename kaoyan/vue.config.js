const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    // 配置跨域
    proxy:'http://127.0.0.1:8000'
        // '/api':{
      //   // 需要代理的地址
      //   target:'http://127.0.0.1:8000/',
      //   // 是否允许跨域
      //   changeOrigin:true,
      //   pathRewrite:{
      //     '^/api':'http://127.0.0.1:8000/'
      //   }
      // }
    
  }

})
