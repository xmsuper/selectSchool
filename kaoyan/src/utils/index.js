/**
 * @param {Function} fn 防抖函数
 * @param {Number} delay 延迟时间
 */
export function debounce(fn, delay) {
	var timer;
	return function() {
		var context = this;
		var args = arguments;
		clearTimeout(timer);
		timer = setTimeout(function() {
			fn.apply(context, args);
		}, delay);
	};
}

/**
 * @param {date} time 需要转换的时间
 * @param {String} fmt 需要转换的格式 如 yyyy-MM-dd、yyyy-MM-dd HH:mm:ss
 */
export function formatTime(time, fmt) {
	if (!time) return '';
	else {
		const date = new Date(time);
		const o = {
			'M+': date.getMonth() + 1,
			'd+': date.getDate(),
			'H+': date.getHours(),
			'm+': date.getMinutes(),
			's+': date.getSeconds(),
			'q+': Math.floor((date.getMonth() + 3) / 3),
			S: date.getMilliseconds(),
			'week': date.getDay()
		};
		if (fmt == 'week') {
			let weekArr = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
			if (o.week == 0) {
				return '星期天'
			}
			return weekArr[o.week - 1]
		}
		if (/(y+)/.test(fmt))
			fmt = fmt.replace(
				RegExp.$1,
				(date.getFullYear() + '').substr(4 - RegExp.$1.length)
			);
		for (const k in o) {
			if (new RegExp('(' + k + ')').test(fmt)) {
				fmt = fmt.replace(
					RegExp.$1,
					RegExp.$1.length === 1 ?
					o[k] :
					('00' + o[k]).substr(('' + o[k]).length)
				);
			}
		}
		return fmt;
	}
}

export function getParams(params) {
	let paramStr = '';
	Object.keys(params)
		.forEach((item) => {
			if (paramStr === '') {
				paramStr = `?${item}=${params[item]}`;
				
			} else {
				paramStr = `${paramStr}&${item}=${params[item]}`;
			}
		});
		paramStr=paramStr.replaceAll(/["]/g,"")  //去除url格式字符串
	return paramStr;
}

function getParamsObj(url) {
	var obj = {};
	if (url.indexOf('?') != -1) {
		var temp1 = url.split('?');
		var pram = temp1[1];
		var keyValue = pram.split('&');
		for (var i = 0; i < keyValue.length; i++) {
			var item = keyValue[i].split('=');
			var key = item[0];
			var value = item[1];
			obj[key] = value;
		}
	}
	return obj;
}
