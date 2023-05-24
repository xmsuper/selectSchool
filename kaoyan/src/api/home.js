import {
	post,
	get,
	put,
	del
} from '@/utils/request'
// /statistics/getSelectRegion

// 获取地址名称列表
export function getAddress() {
	return get('/schoolSelect/main/getAreaName');
}
//获取地址下的学校列表
export function getAddressSchool(data) {
	return get('/schoolSelect/main/getSchoolList',data);
}

export function authRegister(query) {
	return post('/user/register/',query);
}