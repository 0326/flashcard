import Vue from 'vue'
import VueMaterial from 'vue-material'
import App from './App'

Vue.use(VueMaterial)
Vue.material.theme.registerAll({
  default: {
    primary: 'cyan',
    accent: 'pink'
  },
  phone: {
    primary: 'indigo',
    accent: 'pink'
  },
  vgreen: {
    primary: 'green',
    accent: 'pink'
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})
