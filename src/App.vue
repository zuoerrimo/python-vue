<template>
  <div id="app" class="container">
    <div class="operation">
      <el-button type="primary" @click="showAddModal">添加</el-button>
    </div>
    <div class="custom-grid">
      <el-table
        :data="users"
        border
        stripe
        style="width: 100%">
        <el-table-column
          prop="id"
          label="编号"
          >
        </el-table-column>
        <el-table-column
          prop="name"
          label="姓名"
          >
        </el-table-column>
        <el-table-column
        fixed="right"
        label="操作"
        width="100">
          <template slot-scope="scope">
            <el-button @click="showModifyModal(scope.row)" type="text" size="small">修改</el-button>
            <el-button @click="del(scope.row)" type="text" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog :title="title" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="编号" :label-width="formLabelWidth">
          <el-input v-model="form.id" auto-complete="off" :disabled="idDisabled"></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input v-model="form.name" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit">确 定</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'App',
    data() {
      return {
        idDisabled: false,
        title: '添加',
        users: [],
        dialogFormVisible: false,
        form: {
          name: '',
          id: '',
        },
        formLabelWidth: '120px'
      }
    },
    methods: {
      showAddModal() {
        this.idDisabled = false
        this.title = '添加'
        this.form.id = ''
        this.form.name = ''
        this.dialogFormVisible = true
      },
      showModifyModal(row) {
        this.idDisabled = true
        this.title = '修改'
        this.form.id = row.id
        this.form.name = row.name
        this.dialogFormVisible = true
      },
      del(row) {
         axios({
            url: `http://127.0.0.1:5000/delUser/${row.id}`,
            method: 'get',
            transformRequest: [function (data) {
              // Do whatever you want to transform the data
              let ret = ''
              for (let it in data) {
                ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
              }
              return ret
            }],
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
          })
          .then((res) => {
            this.dialogFormVisible = false
            this.users = res.data.users.map((user) => {
                return {
                  id: user[0],
                  name: user[1]
                }
              })
          }, (rej) => {
            this.dialogFormVisible = false
            console.log(rej)
            })
      },
      add() {
        axios({
          url: 'http://127.0.0.1:5000/addUser',
          method: 'post',
          data: {
            ...this.form
          },
          transformRequest: [function (data) {
            // Do whatever you want to transform the data
            let ret = ''
            for (let it in data) {
              ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
            }
            return ret
          }],
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
        .then((res) => {
          this.dialogFormVisible = false
          this.users = res.data.users.map((user) => {
              return {
                id: user[0],
                name: user[1]
              }
            })
        }, (rej) => {
          this.dialogFormVisible = false
          console.log(rej)
          })
      },
      modify() {
        axios({
          url: `http://127.0.0.1:5000/modifyUser/${this.form.id}`,
          method: 'post',
          data: {
            username: this.form.name
          },
          transformRequest: [function (data) {
            // Do whatever you want to transform the data
            let ret = ''
            for (let it in data) {
              ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
            }
            return ret
          }],
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
        .then((res) => {
          this.dialogFormVisible = false
          this.users = res.data.users.map((user) => {
              return {
                id: user[0],
                name: user[1]
              }
            })
        }, (rej) => {
          this.dialogFormVisible = false
          console.log(rej)
          })
      },
      onSubmit() {
        if (this.idDisabled) { // 修改
          this.modify()
        } else { // 添加
          this.add()
        }
      },
      getUsers() {
        axios
        .get('http://127.0.0.1:5000/userList')
        .then((res) => {
          this.users = res.data.users.map((user) => {
            return {
              id: user[0],
              name: user[1],
            }
          })
        })
      },
    },
    mounted() {
      this.getUsers()
    }
  }
</script>
<style>
  .container {
    margin: 10px;
  }
  .operation {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
  }
</style>
