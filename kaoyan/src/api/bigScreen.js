import {
	post,
	get,
	put,
	del
} from '@/utils/request'
// /statistics/getSelectRegion

// 获取前10学校坐标
export function getTop10School() {
	return get('/schoolSelect/bigS/getTop10School');
}
// 获取各省份学校数量
export function countSchoolByProvince() {
	return get('/schoolSelect/bigS/countSchoolByProvince');
}
// 获取用户总人数
export function countUser() {
	return get('/schoolSelect/bigS/countUser');
}
//获取学校总数
export function countSchool() {
	return get('/schoolSelect/bigS/countSchool');
}
//获取分数线
export function countScoreLine() {
	return get('/schoolSelect/bigS/countScoreLine');
}
// 获取学校列表
export function getSchoolList() {
	return get('/schoolSelect/bigS/getSchoolList');
}
// 获得各学校招人人数
export function getSchoolPeoCount() {
	return get('/schoolSelect/bigS/getSchoolPeoCount');
}