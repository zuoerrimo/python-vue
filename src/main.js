import Vue from 'vue'
import App from './App'
import Table from 'element-ui/lib/table'
import TableColumn from 'element-ui/lib/table-column'
Vue.use(Table)
Vue.use(TableColumn)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
