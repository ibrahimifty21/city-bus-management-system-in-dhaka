<template>
    <div>
        <div class="container">
        <div class="card" style="width: 30rem;">
        <div class="card-header my-3">
            <h2>Login</h2>
        </div>
        <div class="card-body">
            <div v-for="data in errors" :key="data.id">
                <div class="row mb-1">
                    <span v-if="data.username" class="info">
                        <i class="fas fa-info-circle"></i>
                    username = {{data.username}}
                    </span>
                    <span v-if="data.password" class="info">
                    <i class="fas fa-info-circle"></i>
                        password = {{data.password}}
                    </span>
                    <span v-if="data.non_field_errors" class="info">
                        <i class="fas fa-info-circle"></i>
                    error = {{data.non_field_errors}}
                    </span>
                </div>
                
                
                
                
                

            </div>
            <form @submit.prevent="submit">
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Username</label>
                    <input type="text" v-model="username" class="form-control" id="exampleInputEmail1" required>
                    
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Password</label>
                    <input type="password" v-model="password" class="form-control" id="exampleInputPassword1" required>
                </div>
                
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck1" required>
                    <label class="form-check-label" for="exampleCheck1">Remeber me</label>

                </div>
                <div class="mb-3 ">
                    <span>Not a member? </span>
                    <router-link to='/register'>
                    Register
                    </router-link>

                </div>

                <button v-if="is_loading === false" type="submit" class="btn btn-primary">Submit</button>
                <button v-if="is_loading === true" class="btn btn-primary" type="button" disabled>
                    <span
                        class="spinner-border spinner-border-sm"
                        role="status"
                        aria-hidden="true"
                    ></span>
                    <span class="visually-hidden">Submitting...</span>
                </button>
            </form>
            
        </div>
    </div>
    
    </div>
    <router-view></router-view>

    </div>
    
    
</template>
<script>
import axios from 'axios'
export default {
    name:'Login',

    data(){
        return{
            username:'',
            password:'',
            errors:[],
            is_loading:false
        }
    },
    methods:{
        async submit(){
            this.is_loading = true
            const formdata = {
                username:this.username,
                password:this.password
            }
            let _this = this
            //console.log(formdata)
            delete  axios.defaults.headers.common["Authorization"];
            this.errors = [];
            await axios.post('api/auth/token/login/',formdata)
            .then(res => {
                this.is_loading = false
                const token = res.data['auth_token']
                // this.$store.dispatch('user',res.data)
                localStorage.setItem('token',token)
                axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
                axios.get('api/auth/users/me/')
                .then(res => {
                    this.$store.dispatch('user',res.data)
                    //console.log(this.$store.state.user)
                    this.$router.push('/')
                })
                .then(err => {
                    console.log(err)
                })
                //console.log(this.$store.state.user.auth_token)
            })
            .catch(function (error) {
                if (error.response) {
                // Request made and server responded
                
                //console.log(error.response.data);
                _this.errors = error.response
                console.log(_this.errors)
                _this.is_loading = false
                
                
                
                } 

            });
        }
    }
}
</script>
<style>
.container{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    
}
.card{
    margin-top: 3rem;
} 
h2{
    font-weight: 900;
}
</style>