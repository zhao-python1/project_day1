import Vue from 'vue'
import Router from 'vue-router'
import Index from "../components/Index";
import Header from "../components/common/Header";
import Bodys from "../components/common/Bodys";
import Footer from "../components/common/Footer";



Vue.use(Router);

export default new Router({
  routes: [
    {
          path: '/',
          name:'Index',
          component:Index,
    },
    // {
    //       path: '/index',
    //       name:'Index',
    //       component:Index,
    // },
    // {
    //       path: '/header',
    //       name:'Header',
    //       component:Header,
    // },
    // {
    //       path: '/bodys',
    //       name:'Bodys',
    //       component:Bodys,
    // },
    // {
    //       path: '/footer',
    //       name:'Footer',
    //       component:Footer,
    // },


  ]
})
