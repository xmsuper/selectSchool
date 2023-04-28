const name2pinyin = {
  安徽大学: 'anhui',
  陕西大学: 'shanxi1',
  澳门大学: 'aomen',
  北京大学: 'beijing',
  重庆大学: 'chongqing',
  福建大学: 'fujian',
  甘肃大学: 'gansu',
  广东大学: 'guangdong',
  广西大学: 'guangxi',
  贵州大学: 'guizhou',
  海南大学: 'hainan',
  河北大学: 'hebei',
  黑龙江大学: 'heilongjiang',
  河南大学: 'henan',
  湖北大学: 'hubei',
  湖南大学: 'hunan',
  江苏大学: 'jiangsu',
  江西大学: 'jiangxi',
  吉林大学: 'jilin',
  辽宁大学: 'liaoning',
  内蒙古大学: 'neimenggu',
  宁夏大学: 'ningxia',
  青海大学: 'qinghai',
  山东大学: 'shandong',
  上海大学: 'shanghai',
  山西大学: 'shanxi',
  四川大学: 'sichuan',
  台湾大学: 'taiwan',
  天津大学: 'tianjin',
  香港大学: 'xianggang',
  新疆大学: 'xinjiang',
  西藏大学: 'xizang',
  云南大学: 'yunnan',
  浙江大学: 'zhejiang',
  
}

export function getProvinceMapInfo (arg) {
  const path = `/static/map/province/${name2pinyin[arg]}.json`
  return {
    key: name2pinyin[arg],
    path: path
  }
}
