const path=require('path')
// 1导入插件，得到构造函数
const HtmlPlugin=require('html-webpack-plugin')
// 2创建插件的实例对象
const htmlPlugin=new HtmlPlugin({
    template:'./src/index.html',
    filename:'./index.html'
})
const {CleanWebpackPlugin}=require('clean-webpack-plugin')
const cleanPlugin= new CleanWebpackPlugin()
module.exports={
    devtool:'eval-source-map',
    mode:'development',
    // 指定文件打包入口
    entry:path.join(__dirname,'./src/index.js'),
    // 指定文件打包出口
    output:{
        // 表示文件的存放输出路劲
        path:path.join(__dirname,'./dist'),
        // 表示输出文件的名称
        filename:'js/bundle.js'
    },
    plugins:[htmlPlugin,cleanPlugin], //3挂载插件的实例对象

    devServer:{
        open:true, //打包完自动打开浏览器
        host:'localhost',
        port:80
    },
    // loader加载器
    module:{
        rules:[
            {test:/\.css$/,use:['style-loader','css-loader']},
            {test:/\.less$/,use:['style-loader','css-loader','less-loader']},
            
        ]
    }
}