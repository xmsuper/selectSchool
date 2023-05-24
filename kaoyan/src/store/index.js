import { createStore } from 'vuex'
import requestFn from '@/api/requestFn'
import createPersistedState from 'vuex-persistedstate'

const getAndCommit=async (url,mutationName,commit,method)=>{
    const {data}=await requestFn({url:url,method:method})
    commit(mutationName,data)
}
const store=createStore({
  state: {
    loading:false,
    isLogin:false,
    current_user:'',
    userInfo:[]
  },
  getters: {
  },
  mutations: {
    setLoading(state,status){
      state.loading=status
    },
    setLogin(state,status){
      state.isLogin=status
    },
    setCurrent_user(state,status){
      state.current_user=status
    },
    setUserInfo(state,status){
      state.userInfo=status
      // console.log(state.userInfo)
    }
  },
  actions: {
    // showAllSchool({commit}){
    //   getAndCommit('/allSchool','setLoading',commit,'get')
    // }
    // login({commit},data){
    //   getAndCommit('/Login','setLoading',commit,'post',data)
    // }
  },
  modules: {
  },
  // 执行持久化登录插件
  plugins:[createPersistedState({
    storage:window.sessionStorage,
    paths:['isLogin','current_user','userInfo']
  })]
})
export default store