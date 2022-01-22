<template>
    

    <div class="container">
        <div class="card" style="width: 30rem;">
        <div class="card-header my-3">
            <h2>Register</h2>
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
                    <span v-if="data.email" class="info">
                        <i class="fas fa-info-circle"></i>
                    email = {{data.email}}
                    </span>
                </div>
                
                
                
                
                

            </div>
            <form @submit.prevent="submit">
                <div class="row">
                    <div class="col">
                        <div class="mb-3">
                            <label for="firstname" class="form-label">First Name</label>
                            <input type="text" v-model="first_name" class="form-control" id="firstname" autocomplete="false">
                    
                        </div>
                    </div>
                    <div class="col">
                        <div class="mb-3">
                            <label for="lastname" class="form-label">Last Name</label>
                            <input type="text" v-model="last_name" class="form-control" id="lastname" autocomplete="false">
                    
                        </div>
                    </div>
                   
                
                </div>
                <div class="mb-3">
                            <label for="username" class="form-label">User Name</label>
                            <input type="text" v-model="username" class="form-control" id="username" required>
                    
                        </div>
                <div class="mb-3">
                            <label for="email" class="form-label">Email</label>
                            <input type="text" v-model="email" class="form-control" id="email" required>
                    
                        </div>

                
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Password</label>
                    <input type="password" v-model="password" class="form-control" id="exampleInputPassword1" required>
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword2" class="form-label">Confirm password
                        <span v-if="confirm_password_sign === true && confirm_password !== ''"><i class="fas fa-check"></i></span>
                    </label>
                    <input type="password" v-model="confirm_password" class="form-control" id="exampleInputPassword2" required>
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
</template>
<script>
import axios from 'axios'
export default {
    data(){
        return{
            first_name:'',
            last_name:'',
            username:'',
            email:'',
            password:'',
            confirm_password:'',
            confirm_password_sign:false,
            errors:[],
            is_loading:false
        }

    },
    watch:{
        confirm_password: function(value){
            if(value === this.password){
                this.confirm_password_sign = true
            }
            else{
                this.confirm_password_sign = false
            }
        }
    },
    methods:{
        async submit(){
            this.is_loading = true
            let _this = this
            const formdata = {
                first_name:this.first_name,
                last_name:this.last_name,
                username:this.username,
                email:this.email,
                password:this.password
            }
            delete  axios.defaults.headers.common["Authorization"];
            this.errors = [];
            await axios.post('api/auth/users/',formdata)
            .then(res =>{
                console.log(res)
                this.is_loading = false
                
                this.$router.push('/login')
            })
            .catch(function (error) {
                if (error.response) {
                // Request made and server responded
                
                //console.log(error.response.data);
                _this.errors = error.response
                console.log(_this.errors)
                
                
                
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
.info{
  color:crimson
}
.fa-check{
    color: rgb(128, 255, 0);
}
</style>