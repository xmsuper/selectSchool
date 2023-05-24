//path是Node内置的路径处理模块
//__dirname:获取当前文件所在目录的绝对路径
// path.resolve:在某一绝对路径的基础上，基于后面的相对路径地址，获取一个全新的绝对路径地址
const path=require('path')
const HtmlWebpackPlugin=require('html-webpack-plugin');
// 清除之前打包的内容
const {CleanWebpackPlugin}= require('clean-webpack-plugin');
const MiniCssExtractPlugin=require('mini-css-extract-plugin');
// 压缩css-js
const CssMinimizerWebpackPlugin=require('css-minimizer-webpack-plugin')
const TerserPlugin=require('terser-webpack-plugin')
// const pageArr=["index","login"],
//     entryObj={},
//     htmlPlugins=[];
// pageArr.forEach(chunk=>{
//     entryObj[chunk]=`./src/${chunk}.js`;
//     htmlPlugins.push(
//         new HtmlWebpackPlugin({
//             //指定页面模板
//             template:`./public/${chunk}.html`,
//             // 打包后的文件的名字
//             filename:`${index}.html`,
//             // 是否压缩
//             minify:true,
//             // 指定导入的资源名称
//             chunks:[chunk]
//         })
//     )
// })
module.exports={
    //production生产环境--会把打包后的js进行自动压缩，NODE_ENV="production"
    // development开发环境--不会压缩
    mode:'development',
    // 默认是index.js，可以改成main.js
    entry:'./src/main.js',
    // 多入口
    // entry:{
    //     index:'./src/index.js',
    //     login:'./src/login.js'
    // }
    output:{
        // 打包后文件的名字
        // [hash]/[hash:8]:为打包后的文件创建哈希名
        // +代码一旦被修改，生成的文件名中的哈希值也会变化
        // +有助于强缓存的设置

        // 多入口为
        // filename:'[name].[hash:8].js'
        filename:"main.[hash:8].js",
        //设置打包的路径[绝对路径]
        path:path.resolve(__dirname,'./dist')
    },

    // 优化项
    optimization:{
        minimizer:[
            new CssMinimizerWebpackPlugin(),
            new TerserPlugin()
        ]
    },

    // 使用插件
    plugins:[
        // 若是用了最上面的
        // ...htmlPlugins
        new HtmlWebpackPlugin({
            //指定页面模板
            template:'./public/index.html',
            // 打包后的文件的名字
            filename:'index.html',
            // 是否压缩
            minify:true,
            // 指定导入的资源名称
            chunks:["index"]
        }),
        // new HtmlWebpackPlugin({
        //     //指定页面模板
        //     template:'./public/login.html',
        //     // 打包后的文件的名字
        //     filename:'login.html',
        //     // 是否压缩
        //     minify:true,
        //     // 指定导入的资源名称
        //     chunks:["login"]
        // })
        // 清除之前打包的内容
        new CleanWebpackPlugin(),
        new MiniCssExtractPlugin({
            //打包后抽离的css文件的名字
            filename:'main.[hash:8].css'
        })
    ],

    // dev-serve
    devServer:{
        host:'127.0.0.1',
        port:3000,
        open:true,
        hot:true,//热更新
        compress:true,//开启服务端的GZIP压缩
        proxy:{
            // /xxx 前缀：主要就是用来区分，以什么为前缀的请求，我们代理到哪台服务器上
            "/api":{
                target:"http:127.0.0.1:8000",
                // 发送请求时：/api/list-->代理服务器--https://www.xxx.com/api/list  [/api 不是真正的地址中的一部分，她就是一个区分的前缀，我们需要把其去掉]
                // 地址重写，主要是把区分前缀从真正的地址中移除掉
                pathRewrite:{"^/api":""},
                changeOrigin:true, //改变源信息
                ws:true  //支持websocket
            }
        }
    },

    // Loader加载器
    module:{
        rules:[{
            test:/\.(css|less)$/,//基于正则匹配
            use:[
                MiniCssExtractPlugin.loader,//抽离css代码
                // "style-loader",//把css以内嵌式导入页面
                "css-loader",//处理特殊语法
                {
                    loader:"postcss-loader",
                    options:{
                        postcssOptions:{
                            plugins:[
                                require("autoprefixer")
                            ]
                        }
                    }
                },//配合autoprefixer&browerlist给css3属性设置前缀【兼容】
                "less-loader"//把less编译为css
            ]
        },{
            test:/\.js$/,
            use:[
                "babel-loader"
            ],
            include:path.resolve(__dirname,'src'),
            exclude:/node_modules/
        },{
            test:/\.(png|jpg?g|gif)$/i,
            type:'javascript/auto', //webpack5需要的
            use:[{
                loader:'url-loader',
                options:{
                    limit:200*1024,
                    esModule:false,
                    // 编译后，没有abse64的图片，编译输出的路径和名称
                    name:'images/[name].[hash:8].[ext]'
                }
            }]
        },{
            test: /\.vue$/,
            use: {
              loader: 'vue-loader',
            }
          }]
    },

    // 设置打包的最大资源大小
    performance:{
        maxAssetSize:100*1024*1024*1024,
        maxEntrypointSize:100*1024*1024*1024
    },
    // 解析器
    resolve:{
        alias:{
            //@以后代表的就是src这个路径
            '@':path.resolve(__dirname,'./src')
        }
    }
}