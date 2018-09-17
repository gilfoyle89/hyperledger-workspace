/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';


import { AdministratorComponent } from './Administrator/Administrator.component';
import { UserComponent } from './User/User.component';

import { getUserDataComponent } from './getUserData/getUserData.component';
import { createUserComponent } from './createUser/createUser.component';
import { deleteUserComponent } from './deleteUser/deleteUser.component';
import { updateUserEncryptedDataComponent } from './updateUserEncryptedData/updateUserEncryptedData.component';
import { grantAccessComponent } from './grantAccess/grantAccess.component';
import { revokeAccessComponent } from './revokeAccess/revokeAccess.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'Administrator', component: AdministratorComponent },
  { path: 'User', component: UserComponent },
  { path: 'getUserData', component: getUserDataComponent },
  { path: 'createUser', component: createUserComponent },
  { path: 'deleteUser', component: deleteUserComponent },
  { path: 'updateUserEncryptedData', component: updateUserEncryptedDataComponent },
  { path: 'grantAccess', component: grantAccessComponent },
  { path: 'revokeAccess', component: revokeAccessComponent },
  { path: '**', redirectTo: '' }
];

@NgModule({
 imports: [RouterModule.forRoot(routes)],
 exports: [RouterModule],
 providers: []
})
export class AppRoutingModule { }
