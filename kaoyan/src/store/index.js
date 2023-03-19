import { createStore } from 'vuex'
import requestFn from '@/api/requestFn'
// const getAndCommit=async (url,mutationName,commit,method)=>{
//     const {data}=await requestFn({url:url,method:method})
//     commit(mutationName,data)
// }
const store=createStore({
  state: {
    loading:false,
    isLogin:false
  },
  getters: {
  },
  mutations: {
    setLoading(state,status){
      state.loading=status
    }
  },
  actions: {
    // showAllSchool({commit}){
    //   getAndCommit('/allSchool','setLoading',commit,'get')
    // }
  },
  modules: {
  }
})
export default store